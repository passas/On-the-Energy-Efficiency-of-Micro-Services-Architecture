## Green Software Development RAPL code

### Requirements
- Debian-based Linux distributions (needs to work with RAPLCap)
- Intel processor
- Non containerized environment

### Required Libraries
1. RAPL
2. lm-sensors
3. Powercap
4. Raplcap

These libraries can be installed with the following command:

```bash
sudo sh raplLibrariesSetup.sh
```

### RAPL executions

Execute the script `measure.sh` to generate the CSV file (this script iterates all the Languages and all of the programs):

```bash
sh measure.sh
```

### CSV file columns

|      Column      |                        Meaning                                                                     |
|:----------------:|:--------------------------------------------------------------------------------------------------:|
|    **Language**  | Programming language                                                                               |
|    **Program**   | Name of program                                                                                    |
|  **PowerLimit**  | Power cap of the cores (in Watts)                                                                  |
|    **Package**   | Energy consumption of the entire socket - all cores consumption, GPU, and external core components |
|     **Core**     | Energy consumption by all cores and caches                                                         |
|     **GPU**      | Energy consumption by the GPU                                                                      |
|     **DRAM**     | Energy consumption by the RAM                                                                      |
|     **Time**     | Algorithm's execution time (in ms)                                                                 |
| **Temperature**  | Mean temperature in all cores (in Celsius degrees)                                                 |
|    **Memory**    | Total physical memory assigned to the algorithm execution (in KBytes)                              |
