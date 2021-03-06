# Copyright 2018 Geoff Lee
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Processor to build a python distutils project"""
import os
import shutil
from zipfile import ZipFile
from subprocess import check_call
# Pylint can't load autopkglib, so stop it moaning
#pylint: disable=locally-disabled,import-error
from autopkglib import Processor, ProcessorError


__all__ = ["PythonBDistBuilder"]

#pylint: disable=locally-disabled,too-few-public-methods
class PythonBDistBuilder(Processor):
    """Build a python disttools project, ready for packaging"""
    description = __doc__
    input_variables = {
        "source_path": {
            "required": True,
            "description": "Path to the source directory of the package.",
        },
    }
    output_variables = {
        "bdist_root": {
            "description": "Root directory of the built distribution",
        },
    }

#pylint: disable=

    def main(self):
        """Build and then unzip the distribution"""
        try:
            os.chdir(self.env['source_path'])
            # Using the system python might produce unexpected
            # results if you are in a virtualenv.
            # Equally, using the virtualenv python might produce
            # unexpected results. The system python is probably
            # what you're expecting.
            check_call(['/usr/bin/python', 'setup.py',
                        'bdist', '-p', 'macOS', '--formats', 'zip'])
            self.output("Built dist at %s" % self.env['source_path'])
        except BaseException, err:
            raise ProcessorError("Can't build dist at %s: %s"
                                 % (self.env['source_path'], err))

        # Now, unzip the built distribution to give us a file hierarchy
        bdist_root = self.env['RECIPE_CACHE_DIR'] + '/bdist_root'

        # Make sure we have a clean target directory
        if os.path.isdir(bdist_root):
            shutil.rmtree(bdist_root)
        try:
            zipped = ZipFile('./dist/' + self.env['NAME'] +
                             '-' + self.env['VERSION'] + '.macOS.zip')
            zipped.extractall(path=bdist_root)
            self.output("Unzipped built distribution root at %s" % bdist_root)
            self.env['bdist_root'] = bdist_root
        except BaseException, err:
            raise ProcessorError("Can't extract built distribution root at %s: %s"
                                 % (bdist_root, err))

if __name__ == '__main__':
    PROCESSOR = PythonBDistBuilder()
    PROCESSOR.execute_shell()
