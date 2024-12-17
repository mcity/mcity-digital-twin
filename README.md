<h1 align="center">
  Mcity Digital Twin
</h1>
Version 1.6.1

![image](https://github.com/user-attachments/assets/42c974c7-7ecf-4a76-ac75-044aef582ab1)

### Flythrough
https://github.com/user-attachments/assets/cea420c1-6b66-40e1-bddf-6a5a55461f54





This digital twin was developed for the University of Michigan’s [Mcity Test Facility](https://mcity.umich.edu/what-we-do/mcity-test-facility/) to support research and development of transportation technology, both academic and commercial. It may be used freely, under the MIT License. To leverage the full set of digital twin capabilities, including live integration with the Mcity Test Facility, please see the [Mcity 2.0](https://mcity.umich.edu/mcity-2-0/) initiative, funded by the National Science Foundation.

https://mcity.umich.edu/

## SYSTEM REQUIREMENTS
* Unreal 4.26
* CARLA 0.9.12+
* Ubuntu 20+ or Windows 10+


## INSTALLATION INSTRUCTIONS

### Source Version of CARLA
Copy the `McityMap` folder inside the `source_version` folder and paste it in this location of your source version of CARLA `Unreal/CarlaUE4/Content/`.

Launch your source version of CARLA and navigate to `Content/McityMap`. Open up the `McityMap_Main` level and enjoy!
![image](https://github.com/user-attachments/assets/31943806-56c8-43bb-9efc-12c8731f056f)
<br>
### Packaged Version of CARLA
Copy the `McityMap` folder inside the `packaged_version/windows` or `packaged_version/linux` directory and paste it in this location of your packaged version of CARLA: `CarlaUE4/Content`. 

Paste the following lines at the bottom of the `CarlaUE4/Config/DefaultGame.ini` file under the `[/Script/UnrealEd.ProjectPackagingSettings]` section.

```
+MapsToCook=(FilePath="/Game/Carla/Maps/McityMap")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/OpenDrive")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/Nav")
```

Launch your packaged version of CARLA, run the `scripts/load_mcity_digital_twin.py` script inside your CARLA python environment and enjoy!


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

## Acknowledgments
* [National Science Foundation](https://www.nsf.gov/)
* [Quantum Signal AI](https://quantumsignalai.com/)
* [CARLA](https://github.com/carla-simulator/carla) 
