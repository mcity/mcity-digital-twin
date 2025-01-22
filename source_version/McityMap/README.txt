# McityMap 1.6.0

## SUMMARY
This map was developed for the University of Michigan’s Mcity testing facility in order to aid in academic research and the development of transportation technology.

https://mcity.umich.edu/

## SYSTEM REQUIREMENTS
* Unreal 4.26
* CARLA 0.9.15

For full system requirements, visit https://github.com/mcity/mcity-digital-twin.

## INSTALLATION INSTRUCTIONS

For full installation instructions, visit https://github.com/mcity/mcity-digital-twin.

## PACKAGE CONTENTS

This package DOES NOT include any CARLA or Unreal code or executeables, only content that can be loaded into an existing CarlaUE4 build.

* McityMap_1_6_0.uasset
	* Dummy material used purely to quickly show the current release version.
* McityMap_Main.umap
	* Main map that contains all props, materials, textures, blueprints, and sublevels.
* Blueprints
	* Contains custom traffic light blueprints based on CARLA's original blueprints, but use custom meshes.
* OpenDrive
	* McityMap_Main.xodr contains the current OpenDrive file provided and maintained by Mcity. 
	* xodr.text contains the current version of the OpenDrive (.xodr) file.
* Static
	* Contains all meshes, materials, and textures, both dynamic and static. 
	* Structure is based on CARLA documentation for use with their semantic segmentation sensors.
* Sublevels
	* CarlaEnvLighting (dynamic)
	* CarlaSigns (dynamic)
	* CarlaTrafficLights (dynamic)
	* McityMap_OpenDrive (dynamic)
	* McityMap_StaticProps (static)
	* McityMap_StaticTrafficLights (static)
	* McityMap_StreetLights (static, hidden)
	* McityMap_Terrain (static)
   
### CONTENT SOURCE NOTES

All 3D static meshes, materials, and textures (with a few exceptions listed below) were created and developed by Quantum Signal AI LLC (QSAI).

https://quantumsignalai.com/

* All foliage and some dynamic traffic sign meshes and textures come from the CARLA asset library.
* All other signage has been created using the MUTCD manual as reference (see credits below under LEGAL).
* Custom traffic light blueprints are based on CARLA's original blueprints, but adapted to use custom QSAI meshes and selected textures.
* T_Perlin_Noise_M.uasset and T_MacroVariation.uasset come from Unreal's Starter Content.
* Original aerial imagery obtained and provided by Mcity and used with permission.

    
## LEGAL

* Unreal® Engine. Unreal® is a trademark or registered trademark of Epic Games, Inc. in the United States of America and elsewhere. Unreal® Engine, Copyright 1998 – 2024, Epic Games, Inc. All rights reserved.

	https://www.unrealengine.com

* CARLA specific code is released under MIT license and specific assets are distributed under CC-BY License.

	https://carla.org/

* University of Michigan logos and markings are trademarked by the University of Michigan and were used with permission.

	https://brand.umich.edu/trademarks-permissions/

* ASAM OpenDrive Standard is © 2024 by ASAM e.V. All Rights Reserved.

	https://www.asam.net/standards/detail/opendrive/

* Manual on Uniform Traffic Control Devices (MUTCD), published by the United States Department of Transportation - Federal Highway Administration.
    
        https://mutcd.fhwa.dot.gov/kno_11th_Edition.htm. 