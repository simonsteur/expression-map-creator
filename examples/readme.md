# Examples

## Example 1

The example_1.yaml file is a simple example of how to create the files required to generate expression maps from.

What we are doing in this example is defining 2 expression maps. One for "Violins 1", which includes the "legato" articulation (on keyswitch 0 (C-2) and on midi channel 1), and the "longs" articulation (on keyswitch 0 (C-2) but on midi channel 2).

We're also creating an expression map for "Violins 2" and including just the legato articulation.

Since there are no other paramters defined in the articulations other than keyswitch and channel. ('ks' and 'chan'), all other values will be set to defaults.

## Example 2

In example_2.yaml we're defining a expression maps for the celli and basses. These include the spicatto articulation but uses an additional parameter to customise it,limiting the max velocity (max-vel).
