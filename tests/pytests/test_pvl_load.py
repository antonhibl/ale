import pytest
import pvl
import ale
import os
import json

from conftest import get_image_kernels, convert_kernels, get_image_label

@pytest.fixture
def test_load_kernels():
    kerns = get_image_kernels('LUA3107H.161')
    updated_kerns, binary_kerns = convert_kernels(kerns)
    yield updated_kerns
    for kern in binary_kerns:
        os.remove(kern)

def test_pvl_load(test_load_kernels):
    cube_label = get_image_label('LUA3107H.161', "isis3")
    isd = ale.loads(cube_label, props={'kernels': test_load_kernels, 'exact_ck_times': False}, only_naif_spice=True, verbose=True)
    isd_obj = json.loads(isd)
    return isd_obj