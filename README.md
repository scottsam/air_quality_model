# Measuring Air Quality

## Overview

This project aims to **design and model data** related to air quality measurement. It focuses on modeling various airborne pollutants such as Nitrogen Monoxide (NO), Nitrogen Dioxide (NO2), and particulate matter (also called particle pollution), which are key contributors to overall air quality, using MSQL database.

For instance, NO2 is measured using micrograms in each cubic meter of air (㎍/m3). A microgram (㎍) is one millionth of a gram. A concentration of 1 ㎍/m3 means that one cubic meter of air contains one microgram of pollutant.

## Air Quality Objectives

To protect public health, the UK Government sets two air quality objectives for NO2 in their Air Quality Strategy:

1. **The Hourly Objective** - The concentration of NO2 in the air, averaged over a period of one hour.
2. **The Annual Objective** - The concentration of NO2 in the air, averaged over a period of a year.

## Hourly Objective Levels and Colour Encoding

The following table shows the colour encoding and the levels for the hourly objective, which represents the mean hourly ratio adopted in the UK:

| NO2 Concentration (㎍/m3) | Air Quality Level | Colour Encoding |
| ------------------------ | ----------------- | --------------- |
| 0 - 67                   | Low               | Green           |
| 68 - 134                 | Moderate          | Yellow          |
| 135 - 200                | High              | Orange          |
| 201+                     | Very High         | Red             |

## The Input Data

The following ZIP file provides data ranging from 1993 to 22 October 2023 taken from 19 monitoring stations in and around Bristol.

Download & save the data file: **Air_Quality_Continous.zip (23.2 Mb)**

1. Create a directory (folder) called `data` on your working machine.
2. Unzip the file there to obtain **Air_Quality_Continuous.csv (112 Mb)**.

Monitors may suffer downtime and may become defunct, so the data isn’t always complete for all stations.

### Sample Data

Shown here is the first 8 lines of the file (cropped):

There are 19 stations (monitors):
```
188 => 'AURN Bristol Centre', 51.4572041156,-2.58564914143
203 => 'Brislington Depot', 51.4417471802,-2.55995583224
206 => 'Rupert Street', 51.4554331987,-2.59626237324
209 => 'IKEA M32', 51.4752847609,-2.56207998299
213 => 'Old Market', 51.4560189999,-2.58348949026
215 => 'Parson Street School', 51.432675707,-2.60495665673
228 => 'Temple Meads Station', 51.4488837041,-2.58447776241
270 => 'Wells Road', 51.4278638883,-2.56374153315
```

These monitors are spread across the four City of Bristol constituencies represented by the following Members of Parliament (MPs):

- **Bristol East** - Kerry McCarthy (MP)
- **Bristol Northwest** - Darren Jones (MP)
- **Bristol South** - Karin Smyth (MP)
- **Bristol West** - Thangam Debbonaire (MP)

Each line represents one reading from a specific detector. Detectors take one reading every hour.

## Data Schema

The schema for the dataset is given below:

| Measure | Description | Unit |
|---------|------------|------|
| Date Time | Date and time of measurement | datetime |
| SiteID | Site ID for the station | integer |
| NOx | Concentration of oxides of nitrogen | ㎍/m3 |
| NO2 | Concentration of nitrogen dioxide | ㎍/m3 |
| NO | Concentration of nitric oxide | ㎍/m3 |
| PM10 | Concentration of particulate matter <10 micron diameter | ㎍/m3 |
| O3 | Concentration of ozone | ㎍/m3 |
| Temperature | Air temperature | °C |
| ObjectID | Object (?) | Integer |
| ObjectID2 | Object (?) | Integer |
| NVPM10 | Concentration of non-volatile particulate matter <10 micron diameter | ㎍/m3 |
| VPM10 | Concentration of volatile particulate matter <10 micron diameter | ㎎/m3 |
| NVPM2.5 | Concentration of non-volatile particulate matter <2.5 micron diameter | ㎍/m3 |
| PM2.5 | Concentration of particulate matter <2.5 micron diameter | ㎍/m3 |
| VPM2.5 | Concentration of volatile particulate matter <2.5 micron diameter | ㎍/m3 |
| CO | Concentration of carbon monoxide | ㎎/m3 |
| RH | Relative Humidity | % |
| Pressure | Air Pressure | mbar |
| SO2 | Concentration of sulphur dioxide | ㎍/m3 |

## Installation & Usage

1. Clone the repository:
   ```sh
   git clone <https://github.com/scottsam/air_quality_model.git>
   ```
2. Navigate to the project directory:
   ```sh
   cd <project-directory>
   ```
3. Follow the setup instructions in the project documentation.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

