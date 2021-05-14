"""
All or portions of this file Copyright (c) Amazon.com, Inc. or its affiliates or
its licensors.

For complete copyright and license terms please see the LICENSE at the root of this
distribution (the "License"). All use of this software is governed by the License,
or, if provided, by the license below or the license accompanying this file. Do not
remove or modify any license notices. This file is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""
import os

import pytest

from Automated.atom_utils import hydra_test_utils as hydra

TEST_DIRECTORY = os.path.dirname(__file__)
EDITOR_TIMEOUT = 180


@pytest.mark.parametrize("project", ["AtomTest"])
@pytest.mark.parametrize("launcher_platform", ['windows_editor'])
@pytest.mark.parametrize("level", ["tmp_level"])
class TestAllComponentsBasicTests(object):

    def test_AllComponentsTest(self, request, editor, level, workspace, project, launcher_platform):
        cfg_args = [level]

        expected_lines = [
            # Decal (Atom) Component
            "Decal (Atom) Entity successfully created",
            "Decal (Atom)_test: Component added to the entity: True",
            "Decal (Atom)_test: Component removed after UNDO: True",
            "Decal (Atom)_test: Component added after REDO: True",
            "Decal (Atom)_test: Entered game mode: True",
            "Decal (Atom)_test: Exit game mode: True",
            "Decal (Atom) Controller|Configuration|Material: SUCCESS",
            "Decal (Atom)_test: Entity is hidden: True",
            "Decal (Atom)_test: Entity is shown: True",
            "Decal (Atom)_test: Entity deleted: True",
            "Decal (Atom)_test: UNDO entity deletion works: True",
            "Decal (Atom)_test: REDO entity deletion works: True",
            # DepthOfField Component
            "DepthOfField Entity successfully created",
            "DepthOfField_test: Component added to the entity: True",
            "DepthOfField_test: Component removed after UNDO: True",
            "DepthOfField_test: Component added after REDO: True",
            "DepthOfField_test: Entered game mode: True",
            "DepthOfField_test: Exit game mode: True",
            "DepthOfField_test: Entity disabled initially: True",
            "DepthOfField_test: Entity enabled after adding required components: True",
            "DepthOfField Controller|Configuration|Camera Entity: SUCCESS",
            "DepthOfField_test: Entity is hidden: True",
            "DepthOfField_test: Entity is shown: True",
            "DepthOfField_test: Entity deleted: True",
            "DepthOfField_test: UNDO entity deletion works: True",
            "DepthOfField_test: REDO entity deletion works: True",
            # Exposure Control Component
            "Exposure Control Entity successfully created",
            "Exposure Control_test: Component added to the entity: True",
            "Exposure Control_test: Component removed after UNDO: True",
            "Exposure Control_test: Component added after REDO: True",
            "Exposure Control_test: Entered game mode: True",
            "Exposure Control_test: Exit game mode: True",
            "Exposure Control_test: Entity disabled initially: True",
            "Exposure Control_test: Entity enabled after adding required components: True",
            "Exposure Control_test: Entity is hidden: True",
            "Exposure Control_test: Entity is shown: True",
            "Exposure Control_test: Entity deleted: True",
            "Exposure Control_test: UNDO entity deletion works: True",
            "Exposure Control_test: REDO entity deletion works: True",
            # Global Skylight (IBL) Component
            "Global Skylight (IBL) Entity successfully created",
            "Global Skylight (IBL)_test: Component added to the entity: True",
            "Global Skylight (IBL)_test: Component removed after UNDO: True",
            "Global Skylight (IBL)_test: Component added after REDO: True",
            "Global Skylight (IBL)_test: Entered game mode: True",
            "Global Skylight (IBL)_test: Exit game mode: True",
            "Global Skylight (IBL) Controller|Configuration|Diffuse Image: SUCCESS",
            "Global Skylight (IBL) Controller|Configuration|Specular Image: SUCCESS",
            "Global Skylight (IBL)_test: Entity is hidden: True",
            "Global Skylight (IBL)_test: Entity is shown: True",
            "Global Skylight (IBL)_test: Entity deleted: True",
            "Global Skylight (IBL)_test: UNDO entity deletion works: True",
            "Global Skylight (IBL)_test: REDO entity deletion works: True",
            # Physical Sky Component
            "Physical Sky Entity successfully created",
            "Physical Sky component was added to entity",
            "Entity has a Physical Sky component",
            "Physical Sky_test: Component added to the entity: True",
            "Physical Sky_test: Component removed after UNDO: True",
            "Physical Sky_test: Component added after REDO: True",
            "Physical Sky_test: Entered game mode: True",
            "Physical Sky_test: Exit game mode: True",
            "Physical Sky_test: Entity is hidden: True",
            "Physical Sky_test: Entity is shown: True",
            "Physical Sky_test: Entity deleted: True",
            "Physical Sky_test: UNDO entity deletion works: True",
            "Physical Sky_test: REDO entity deletion works: True",
            # PostFX Layer Component
            "PostFX Layer Entity successfully created",
            "PostFX Layer_test: Component added to the entity: True",
            "PostFX Layer_test: Component removed after UNDO: True",
            "PostFX Layer_test: Component added after REDO: True",
            "PostFX Layer_test: Entered game mode: True",
            "PostFX Layer_test: Exit game mode: True",
            "PostFX Layer_test: Entity is hidden: True",
            "PostFX Layer_test: Entity is shown: True",
            "PostFX Layer_test: Entity deleted: True",
            "PostFX Layer_test: UNDO entity deletion works: True",
            "PostFX Layer_test: REDO entity deletion works: True",
            # Radius Weight Modifier Component
            "Radius Weight Modifier Entity successfully created",
            "Radius Weight Modifier_test: Component added to the entity: True",
            "Radius Weight Modifier_test: Component removed after UNDO: True",
            "Radius Weight Modifier_test: Component added after REDO: True",
            "Radius Weight Modifier_test: Entered game mode: True",
            "Radius Weight Modifier_test: Exit game mode: True",
            "Radius Weight Modifier_test: Entity is hidden: True",
            "Radius Weight Modifier_test: Entity is shown: True",
            "Radius Weight Modifier_test: Entity deleted: True",
            "Radius Weight Modifier_test: UNDO entity deletion works: True",
            "Radius Weight Modifier_test: REDO entity deletion works: True",
            # Light Component
            "Light Entity successfully created",
            "Light_test: Component added to the entity: True",
            "Light_test: Component removed after UNDO: True",
            "Light_test: Component added after REDO: True",
            "Light_test: Entered game mode: True",
            "Light_test: Exit game mode: True",
            "Light_test: Entity is hidden: True",
            "Light_test: Entity is shown: True",
            "Light_test: Entity deleted: True",
            "Light_test: UNDO entity deletion works: True",
            "Light_test: REDO entity deletion works: True",
            # Display Mapper Component
            "Display Mapper Entity successfully created",
            "Display Mapper_test: Component added to the entity: True",
            "Display Mapper_test: Component removed after UNDO: True",
            "Display Mapper_test: Component added after REDO: True",
            "Display Mapper_test: Entered game mode: True",
            "Display Mapper_test: Exit game mode: True",
            "Display Mapper_test: Entity is hidden: True",
            "Display Mapper_test: Entity is shown: True",
            "Display Mapper_test: Entity deleted: True",
            "Display Mapper_test: UNDO entity deletion works: True",
            "Display Mapper_test: REDO entity deletion works: True",
            # Reflection Probe Component
            "Reflection Probe Entity successfully created",
            "Reflection Probe_test: Component added to the entity: True",
            "Reflection Probe_test: Component removed after UNDO: True",
            "Reflection Probe_test: Component added after REDO: True",
            "Reflection Probe_test: Entered game mode: True",
            "Reflection Probe_test: Exit game mode: True",
            "Reflection Probe_test: Entity disabled initially: True",
            "Reflection Probe_test: Entity enabled after adding required components: True",
            "Reflection Probe_test: Entity is hidden: True",
            "Reflection Probe_test: Entity is shown: True",
            "Reflection Probe_test: Entity deleted: True",
            "Reflection Probe_test: UNDO entity deletion works: True",
            "Reflection Probe_test: REDO entity deletion works: True",
            "Reflection Probe_test: Cubemap is generated: True",
        ]

        unexpected_lines = [
            "failed to open",
            "Traceback (most recent call last):",
        ]

        hydra.launch_and_validate_results(
            request,
            TEST_DIRECTORY,
            editor,
            "AllComponentsBasicTests_test_case.py",
            timeout=EDITOR_TIMEOUT,
            expected_lines=expected_lines,
            unexpected_lines=unexpected_lines,
            halt_on_unexpected=True,
            cfg_args=cfg_args,
        )
