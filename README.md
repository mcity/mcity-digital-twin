<div align="center">
  <a href="https://mcity.umich.edu/">
    <!--     ![mcity_logo](https://github.com/user-attachments/assets/fab191e1-1047-488e-bd36-9298c67a6236) -->
    <img style="max-width=50% !important;" src="https://github.com/user-attachments/assets/fab191e1-1047-488e-bd36-9298c67a6236">
  </a>
</div>
<h1 align="center">
  Mcity Digital Twin
</h1>

## Prerequirements

- CARLA installed. * If using Windows, you will only be able to install digital twin on the source version of CARLA.
- Python 3+ enviornment to use CARLA API.

## Installation Steps
### Source Version of CARLA
Copy the `McityMap` folder inside the `source_version` folder and paste it in this location of your source version of CARLA `Unreal/CarlaUE4/Content/`.

Launch your source version of CARLA and navigate to `Content/McityMap`. Open up the `McityMap_Main` level and enjoy!
![image](https://github.com/user-attachments/assets/31943806-56c8-43bb-9efc-12c8731f056f)
<br>
### Packaged Version of CARLA
Copy the `McityMap` folder inside the `packaged_version` folder and paste it in this location of your packaged version of CARLA `CarlaUE4/Content`.

Paste the following lines at the bottom of the `CarlaUE4/Config/DefaultGame.ini` file under the `[/Script/UnrealEd.ProjectPackagingSettings]` section.

```
+MapsToCook=(FilePath="/Game/Carla/Maps/McityMap")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/OpenDrive")
+DirectoriesToAlwaysStageAsUFS=(Path="McityMap/Nav")
```

Launch your packaged version of CARLA and run the `scritps/load_mcity_digital_twin.py` script inside your CARLA python enviornment and enjoy!
