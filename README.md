<h1 align="center">
  Mcity Digital Twin
</h1>
Version 1.6.1

![image](https://github.com/user-attachments/assets/42c974c7-7ecf-4a76-ac75-044aef582ab1)

### Flythrough
https://github.com/user-attachments/assets/015a96be-20f2-46a6-8d56-70d5f74790f4





This digital twin was developed for the University of Michigan’s [Mcity Test Facility](https://mcity.umich.edu/what-we-do/mcity-test-facility/) to support research and development of transportation technology, both academic and commercial. It may be used freely, under the MIT License. To leverage the full set of digital twin capabilities, including live integration with the Mcity Test Facility, please see the [Mcity 2.0](https://mcity.umich.edu/mcity-2-0/) initiative, funded by the National Science Foundation.

https://mcity.umich.edu/

## SYSTEM REQUIREMENTS
#### OMNIVERSE
* GeForce RTX 3070+
* 16GB RAM
* An [Omniverse](https://www.nvidia.com/en-us/omniverse/) Blueprint, application or service.
#### CARLA
* Unreal 4.26
* CARLA 0.9.12+
* Ubuntu 20+ or Windows 10+
* [Git LFS](https://git-lfs.com/)
* 6GB+ GPU

In order to download the files properly, you will need to have [Git LFS](https://git-lfs.com/) installed.
Once installed, you can run the installation commands to clone or pull the available content.

## OMNIVERSE DIGITAL TWIN INSTALLATION INSTRUCTIONS
Copy the `Omniverse/Collected_Mcity_NSR_v4_1_6` folder to your desired location. Open `McityMap_Main.usdc` stage in any Omniverse Blueprint, application or service and enjoy!

## CARLA DIGITAL TWIN INSTALLATION INSTRUCTIONS

Download the content for the first time.
```
git lfs clone https://github.com/mcity/mcity-digital-twin.git
```

Pull in new content.
```
git lfs pull
```

### Source Version of CARLA
Copy the `McityMap` folder inside the `CARLA/source_version` folder and paste it in this location of your source version of CARLA `Unreal/CarlaUE4/Content/`.

Launch your source version of CARLA and navigate to `Content/McityMap`. Open up the `McityMap_Main` level and enjoy!
![image](https://github.com/user-attachments/assets/31943806-56c8-43bb-9efc-12c8731f056f)
<br>
### Packaged Version of CARLA
Create an `McityMap` folder inside your packaged version of CARLA at this location `CarlaUE4/Content`. Then copy the contents inside of the `CARLA/packaged_version/windows` or `CARLA/packaged_version/linux` directory and paste it here: `CarlaUE4/Content/McityMap`. 

Paste the following lines at the bottom of the `CarlaUE4/Config/DefaultGame.ini` file under the `[/Script/UnrealEd.ProjectPackagingSettings]` section.

```
+MapsToCook=(FilePath="/Game/Carla/Maps/McityMap")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/OpenDrive")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/Nav")
```

Launch your packaged version of CARLA, run the `CARLA/scripts/load_mcity_digital_twin.py` script inside your CARLA python environment and enjoy!

## PARALLEL DOMAIN DIGITAL TWIN
<a href="https://www.diffchecker.com/image-compare/qRpxUOBJ/" target="_blank" rel="noopener noreferrer">
<img width="1636" height="1021" alt="real_vs_pd-replica" src="https://github.com/user-attachments/assets/754ee2e9-b9ea-45f6-9dc9-58652f327225" />
</a>
The Mcity Digital Twin by Parallel Domain is a high-fidelity, photorealistic simulation of the University of Michigan’s world-class Mcity Test Facility. Created using PD Replica technology, it translates real-world track data into a pixel-accurate virtual environment designed for advanced Physical AI research. This digital twin allows developers to test the entire autonomous vehicle stack—from perception to control—under a wide range of programmable weather and lighting conditions. By bridging the gap between simulation and reality, it enables researchers to safely and at scale validate complex edge cases before moving to the physical track.
[Request Access To The Parallel Domain Digital Twin](https://paralleldomain.com/new-mcity-digital-twin-by-parallel-domain-brings-physical-ai-research-closer-to-reality)

### KNOWN ISSUES
#### Omniverse Digital Twin
- When using the Asset Validator (v0.16.2), you will get the following error for the GroundTruthCapabilityChecker:
  - "SemanticsAPI schema is applied but QCode is not authored." This can be ignored.


### MCITY TEST FACILITY DATASETS

Below are example datasets from the Mcity Test Facility. There are two types: one real-world and one synthetic. The real-world dataset includes 6 [Triton – 2.3 MP Sony IMX392 CMOS](https://thinklucid.com/product/triton-23-mp-imx392/?srsltid=AfmBOooNnkvhosWvZXCi-G9NkdK1845-vA-5GbgraWZNhR4th0h6TReg) on-vehicle camera sensors, 1 [RoboSense P6 Solid State Lidar](https://www.robosense.ai/en/rslidar/RS-Fusion-P6) that publishes 6 lidar topics, and 1 point cloud track scan of the Mcity Facility. The synthetic dataset was generated using [NVIDIA Omniverse Sensor RTX](https://blogs.nvidia.com/blog/omniverse-sensor-rtx-autonomous-machines/) inside our Mcity Omniverse Digital Twin. It includes 6 cameras and 4 solid-state lidars. If you would like access to the full dataset, please email mcity-engineering@umich.edu.

Example Datasets: https://drive.google.com/drive/folders/1N4zK63B4GQT-LRQyEyrU_KwLh4ULf2Uu?usp=drive_link

Real-World
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/337895ee-a61c-46dd-bcf2-97477f4e3fbf" />
NVIDIA Omniverse Sensor RTX
<img width="1620" height="1512" alt="image" src="https://github.com/user-attachments/assets/7d6f11dd-6410-47b8-80dc-2c71f8f44495" />

## PACKAGE CONTENTS

This package DOES NOT include any CARLA or Unreal code or executables, only content that can be loaded into an existing CarlaUE4 build.

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

* Unreal® Engine. Unreal® is a trademark or registered trademark of Epic Games, Inc. in the United States of America and elsewhere. Unreal® Engine, Copyright 1998 – 2025, Epic Games, Inc. All rights reserved.

	https://www.unrealengine.com

* CARLA specific code is released under MIT license and specific assets are distributed under CC-BY License.

	https://carla.org/

* University of Michigan logos and markings are trademarked by the University of Michigan and were used with permission.

	https://brand.umich.edu/trademarks-permissions/

* ASAM OpenDrive Standard is © 2025 by ASAM e.V. All Rights Reserved.

	https://www.asam.net/standards/detail/opendrive/

* Manual on Uniform Traffic Control Devices (MUTCD), published by the United States Department of Transportation - Federal Highway Administration.
    
        https://mutcd.fhwa.dot.gov/kno_11th_Edition.htm. 

## Acknowledgments
* [National Science Foundation](https://www.nsf.gov/)
* [Quantum Signal AI](https://quantumsignalai.com/)
* [CARLA](https://github.com/carla-simulator/carla) 
