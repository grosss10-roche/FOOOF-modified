"""Objects sub-module, for model objects and functions that operate on model objects."""

from .fit import SpectralModel
from .group import SpectralGroupModel
from .utils import (compare_model_objs, average_group, average_reconstructions,
                    combine_model_objs, fit_models_3d)
