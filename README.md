# SHMU Python Automatic Temperature Downloader

Python script for downloading daily maximum temperature data from the **Slovak Hydrometeorological Institute (SHMÚ)** and saving it to a CSV file.

## Features

* Downloads temperature data from SHMÚ
* Extracts daily maximum temperatures
* Converts timestamps to dates
* Saves data to `teploty.csv`
* Prevents duplicate dates

## Requirements

Python 3 and the following libraries:

```bash
pip install requests pandas
```

## Usage

Clone the repository:

```bash
git clone https://github.com/Setlers/SHMU_Python_automatic_temperature_downloader.git
cd SHMU_Python_automatic_temperature_downloader
```

Run the script:

```bash
SHMU_automatik_temperature_downloader.py
```

The results are saved to:

```text
teploty.csv
```

Example:

```csv
datum,teplota
2026-09-07,24.8
2026-09-08,26.1
2026-09-09,25.3
```

## Data source

Data is obtained from the official **Slovak Hydrometeorological Institute (SHMÚ)** website:

https://www.shmu.sk/

## License

No license has been selected yet.
