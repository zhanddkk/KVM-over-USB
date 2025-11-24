import subprocess
import shutil
import os
import pathlib
import datetime
import time
import zipfile
from project_info import *

_build_dir = '_build_dir'
_version = VERSION
_app_name = 'usb_kvm'
_proj_path = pathlib.Path(__file__).as_posix()
_build_no = '{}-{:0>8X}'.format(datetime.datetime.now().strftime('%Y-%m-%d'), int(time.time()))
_build_info_filename = pathlib.Path(_build_dir) / '_build_info.txt'

class MakeOpt:
    @staticmethod
    def do_zip_folder(folder_path, zip_path):
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for _root, _, _files in os.walk(folder_path):
                for _file in _files:
                    _file_path = os.path.join(_root, _file)
                    _arc_name = os.path.relpath(_file_path, folder_path)
                    zipf.write(_file_path, _arc_name, compress_type=zipfile.ZIP_DEFLATED)
                    pass
                pass
            pass

    @classmethod
    def do_build(cls):
        _entry = '{}/{}.py'.format(_build_dir, _app_name)
        if pathlib.Path(_build_dir).is_dir():
            cls.do_clean()
            pass
        os.makedirs(_build_dir, exist_ok=True)

        with open(_entry, 'w', encoding='utf-8') as _if:
            # for _k, _v in os.environ.items():
            #     print('{:<32}: {}'.format(_k, _v))
            #     pass
            _if.write('import os\nos.environ[\'PYTHONPATH\']=\'{}\'\n'.format(_proj_path))
            _if.write('_build_no = \'{}\'\n'.format(_build_no))
            _if.write('if __name__ == \'__main__\':\n')
            _if.write('    from usb_kvm_client import entry as _entry\n')
            _if.write('    _entry(_build_no)\n')
            _if.write('    pass\n')
            pass
        _ret = subprocess.run(
            [
                'python', '-m', 'nuitka',
                '--standalone',
                '--enable-plugin=pyside6',
                '--company-name=Themovif',
                '--product-name=USB KVM',
                '--file-version=1.0.0.0',
                '--product-version={}'.format(_version),
                '--copyright=Copyright © 沐雨迎风工作室',
                '--windows-icon-from-ico=./icons/app.ico',
                '--windows-file-description=a open source usb kvm client',
                '--windows-console-mode=disable',
                '--include-qt-plugins=multimedia',
                '--include-data-dir=./icons=icons',
                '--include-data-dir=./data=data',
                '--include-data-dir=./translate=translate',
                '--noinclude-dlls=libQt6Charts*',
                '--noinclude-dlls=libQt6Quick3D*',
                '--noinclude-dlls=libQt6Sensors*',
                '--noinclude-dlls=libQt6Test*',
                '--noinclude-dlls=libQt6WebEngine*',
                '--noinclude-dlls=qt6web*',
                '--noinclude-dlls=qt6pdf*',
                '--output-filename={}.exe'.format(_app_name),
                '--output-dir={}'.format(_build_dir),
                _entry
            ]
        )
        if _build_info_filename.exists():
            shutil.rmtree(_build_info_filename)
            pass
        if _ret.returncode == 0:
            with open(_build_info_filename, 'w', encoding='utf-8') as _f:
                _f.write(_build_no)
                pass
            pass
        pass

    @classmethod
    def do_clean(cls):
        shutil.rmtree(_build_dir, ignore_errors=True)
        pass

    @classmethod
    def do_package(cls):
        if _build_info_filename.exists():
            _build_info = _build_info_filename.read_text(encoding='utf-8')
            pass
        else:
            return
        cls.do_zip_folder('{}/{}.dist'.format(_build_dir, _app_name),
                          '{}/{}-{}_{}.zip'.format(_build_dir,
                                                   _app_name,
                                                   _version,
                                                   _build_info))
        pass
    pass


if __name__ == '__main__':
    import sys
    try:
        cmd = sys.argv[1]
        pass
    except IndexError:
        cmd = None
        pass
    mk = MakeOpt()
    if cmd == 'clean':
        mk.do_clean()
        pass
    elif cmd == 'package':
        mk.do_package()
        pass
    elif cmd == 'app':
        mk.do_build()
        pass
    elif cmd == 'all':
        mk.do_build()
        mk.do_package()
        pass
    else:
        mk.do_clean()
        mk.do_build()
        mk.do_package()
        pass
    pass
