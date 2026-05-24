import anndata as ad
from typing import Union, Sequence, Optional, Dict, Tuple
import numpy as np
import pandas as df

def copy_feature_score_to_obs(
    patch_table: ad.AnnData,
    feature_name: str,
    obs_colname: Optional[str] = None,
) -> ad.AnnData:
    """
    Copy one feature score from ``patch_table[:, feature_name].X`` into ``patch_table.obs``.

    Parameters
    ----------
    patch_table : AnnData
        Patch-level AnnData table.
    feature_name : str
        Feature name in ``patch_table.var_names``.
    obs_colname : str, optional
        Output column name in ``patch_table.obs``. Defaults to ``feature_name``.

    Returns
    -------
    patch_table : AnnData
        The same AnnData object, modified in place.
    """
    if feature_name not in patch_table.var_names:
        raise KeyError(
            f"Feature '{feature_name}' not found in patch_table.var_names."
        )

    if obs_colname is None:
        obs_colname = feature_name

    x = patch_table[:, feature_name].X
    if hasattr(x, "toarray"):
        scores = x.toarray()[:, 0]
    else:
        scores = np.asarray(x).reshape(-1)

    patch_table.obs[obs_colname] = scores
    return patch_table



def interpolate_patch_max(
    samples: Dict[Tuple[int, int], float],
    height: int,
    width: int,
    patch_size: int,
    downsample: int = 1,
) -> np.ndarray:
    """
    Rasterize sparse sample scores by painting filled squares of size
    ``patch_size`` centred on each sample coordinate.  Patches are drawn
    in ascending score order so the highest score wins on overlap.

    Parameters
    ----------
    samples : Dict[Tuple[int, int], float]
        Dictionary mapping (x, y) pixel coordinates to scalar scores.
    height : int
        Full-resolution canvas height.
    width : int
        Full-resolution canvas width.
    patch_size : int
        Side length (in full-resolution pixels) of each painted square.
    downsample : int, default=1
        Factor by which to downsample the canvas before painting.
        Coordinates and patch_size are scaled accordingly.

    Returns
    -------
    out : np.ndarray, shape (out_height, out_width), dtype float32
        Rasterized score map; background pixels are 0.
    """
    out_height = height // downsample
    out_width  = width  // downsample
    half       = (patch_size // downsample) // 2

    out = np.zeros((out_height, out_width), dtype=np.float32)

    # Sort ascending so highest score is painted last (wins on overlap)
    coords  = np.array(list(samples.keys()))   # (N, 2)  col=x, row=y
    scores  = np.array(list(samples.values()), dtype=np.float32)  # (N,)
    order   = np.argsort(scores)

    for idx in order:
        x, y = coords[idx]
        score = scores[idx]

        xi = int(round(x / downsample))
        yi = int(round(y / downsample))

        x0 = max(xi - half, 0)
        x1 = min(xi + half, out_width  - 1)
        y0 = max(yi - half, 0)
        y1 = min(yi + half, out_height - 1)

        out[y0:y1, x0:x1] = score

    return out