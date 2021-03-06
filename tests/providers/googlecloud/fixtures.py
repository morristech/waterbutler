import os

import pytest

from waterbutler.core.path import WaterButlerPath


@pytest.fixture()
def mock_auth():
    return {
        'name': 'Roger Deng',
        'email': 'roger@deng.com'
    }


@pytest.fixture()
def mock_auth_2():
    return {
        'name': 'Deng Roger',
        'email': 'deng@roger.com'
    }


@pytest.fixture()
def mock_creds():
    return {
        'token': 'GlxLBdGqh56rEStTEs0KeMdEFmRJlGpg7e95y8jvzQoHbFZrnPDNB'
    }


@pytest.fixture()
def mock_creds_2():
    return {
        'token': 'eMdEFmRJlGpg7e95y8jvzQoHbFZrnPDNBsYTIG2txg8SmacwtERkU'
    }


@pytest.fixture()
def mock_settings():
    return {
        'bucket': 'gcloud-test.longzechen.com',
        'region': 'US-EAST1'
    }


@pytest.fixture()
def mock_settings_2():
    return {
        'bucket': 'gcloud-test-2.longzechen.com',
        'region': 'US-EAST1'
    }


@pytest.fixture()
def file_wb_path():
    return WaterButlerPath('/test-folder-1-copy/DSC_0235.JPG')


@pytest.fixture()
def src_file_wb_path():
    return WaterButlerPath('/test-folder-1/DSC_0244.JPG')


@pytest.fixture()
def dest_file_wb_path():
    return WaterButlerPath('/test-folder-1/DSC_0244_COPY.JPG')


@pytest.fixture()
def folder_path():
    return '/test-folder-1/'


@pytest.fixture()
def sub_folder_1_path():
    return '/test-folder-1/test-folder-5/'


@pytest.fixture()
def sub_folder_2_path():
    return '/test-folder-1/test-folder-6/'


@pytest.fixture()
def sub_file_1_path():
    return '/test-folder-1/DSC_0235.JPG'


@pytest.fixture()
def sub_file_2_path():
    return '/test-folder-1/DSC_0244.JPG'


@pytest.fixture()
def file_path():
    return '/test-folder-1/DSC_0235.JPG'


@pytest.fixture()
def dest_file_path():
    return '/test-folder-2/DSC_0235_2.JPG'


@pytest.fixture()
def src_folder_wb_path():
    return WaterButlerPath('/test-folder-1/')


@pytest.fixture()
def src_file_obj_name():
    return 'test-folder-1/DSC_0244.JPG'


@pytest.fixture()
def dest_file_obj_name():
    return 'test-folder-1-copy/DSC_0244.JPG'


@pytest.fixture()
def src_folder_obj_name():
    return 'test-folder-1/'


@pytest.fixture()
def dest_folder_obj_name():
    return 'test-folder-1-copy/'


@pytest.fixture
def test_file_1():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/files/DSC_0235.JPG'
            ),
            'rb'
    ) as fp:
        return fp.read()


@pytest.fixture
def test_file_2():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/files/DSC_0244.JPG'
            ),
            'rb'
    ) as fp:
        return fp.read()


@pytest.fixture()
def meta_folder_itself():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/metadata/folder-itself.json'
            ),
            'r'
    ) as fp:
        return fp.read()


@pytest.fixture()
def meta_folder_all():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/metadata/folder-all.json'
            ),
            'r'
    ) as fp:
        return fp.read()


@pytest.fixture()
def meta_file_itself():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/metadata/file-itself.json'
            ),
            'r'
    ) as fp:
        return fp.read()


@pytest.fixture()
def meta_file_extra():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/metadata/file-extra.json'
            ),
            'r'
    ) as fp:
        return fp.read()


@pytest.fixture()
def err_resp_unauthorized():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/errors/401-unauthorized.json'
            ),
            'r'
    ) as fp:
        return fp.read()


@pytest.fixture()
def err_resp_not_found():

    with open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/errors/404-not-found.json'
            ),
            'r'
    ) as fp:
        return fp.read()
