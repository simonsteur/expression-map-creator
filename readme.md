# Expression Map Creator

Expression Map Creator (EMC) is a tool for quickly creating expression maps for use in Cubase. 

The reason for the creation of this tool is to save time setting up and maintaining expression maps, which is a cumbersome manual process.
To achieve this EMC loads instruments and the articulations (+ additional information like keyswitches, midi channel, etc.) from a single or a collection of yaml files. This allows you to quickly copy those yaml files and adjust per instrument/library. You can use that same file to do any updates to your expression maps, and then just regenerate the expression map for it.

## How to install

### Download binary for your OS

The latest versions of EMC are compiled for both windows and OSX so that you may just download a single binary file, you can find those here: (INSERT LINK)

<!-- ### clone git repo and run source code

You may also clone this git repo and run the source code directly, just make sure you have atleast python version 3.5 installed. -->

## How to use

Create one or multiple yaml files that maps the instruments and articulations you want to create an expression map for. Use the following syntax:

```language
map:
  SSS Violins 1:
    legato:
      ks: 0
      chan: 1
  SSS Violins 2:
    long-cs:
      ks: 1
      chan: 2
```

### Parameters

You can specify several parameters per articulation, this way you can control the midi actions. These parameters are the following (defaults are cubase defaults):

| parameter     | usage                         | default |
| :-------------|:----------------------------- | :------ |
| ks            | midi note number for the articulations keyswitch (example: C-2 = 0) | 0
| chan          | midi channel | 1
| vel           | velocity  | 1
| length        | length | 1
| min-vel       | minimum velocity | 0
| max-vel       | maximum velocity | 127
| min-pitch     | minimum pitch | 0
| max-pitch     | maximum pitch | 127
| transpose     | transpose | 0
| remote        | keyswitch to assign as remote to the articulation | starts at 0 (C-2), then counts up from there.

#### Midi note numbers (C3=60 mapping)

| octave | C | C# | D | D# | E | F | F# | G | G# | A | A# | B |
| :----- |:--|:---|:--|:---|:--|:--|:---|:--|:---|:--|:---|:--|
| -2 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
| -1 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23
| 0 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |33 | 34 | 35
| 1 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47
| 2 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59
| 3 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71
| 4 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83
| 5 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95
| 6 | 96 | 97 | 98 | 99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 | 107 |
| 7 | 108 | 109 | 110 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119
| 8 | 120 | 121 | 122 | 123 | 124 | 125 | 126 | 127
