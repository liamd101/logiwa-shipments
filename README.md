# Logiwa Shipment Data

A Python script for retrieving data from the Logiwa WMS Shipment Order API and storing it in a series of SQL tables.

## Documentation

The API response data classes are documented in `models/datastructs.py`.
Each class in this file corresponds to a SQL table.
The `models` subdirectory also contains helper functions and classes for serializing data into SQL supported formats

This currently stages data in a `.jsonl` file, but can be modified to write to a SQL table instead for easier querying.

## Usage

This script was built using `uv`.
To run the script, run
```bash
git clone git@github.com:liamd101/logiwa-shipments
cd logiwa-shipments
uv run -- main.py
```

