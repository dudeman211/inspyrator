/**
 * inspyrator.js
 * A script to build scales of the 7 major modes
 * from the 12-note chromatic scale.
 *
 *
 * @licence MIT, LICENSE.txt, https://opensource.org/licenses/MIT
 * @version 0.01a
 * @author Sal Bruno
 */

var chromatic = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];

var baseMode = [2, 2, 1, 2, 2, 2, 1];

var modes = [
    'Ionian (Major)',
    'Dorian',
    'Phrygian',
    'Lydian',
    'Mixolydian',
    'Aeolian (minor)',
    'Locrian'
];

var selectedKeyDropDown = document.getElementById('notes');
var selectedKeyIndex;
var selectedKey;

function changeLabel() {
    selectedKeyIndex = selectedKeyDropDown.selectedIndex;
    selectedKey = selectedKeyDropDown.options[selectedKeyIndex].text;
    document.getElementById('selectedKeyLabel').innerHTML = 'Working Key is: ' + selectedKey;
}
function makeNewChromatic() {
    var newChromatic = chromatic.slice(selectedKeyIndex).concat(chromatic.slice(0, selectedKeyIndex));
    newChromatic.push(selectedKey);

    return newChromatic;
}
function changeModes(index) {
    return baseMode.slice(index).concat(baseMode.slice(0, index));
}
function buildScales() {
    var scalePara = document.getElementsByClassName('scale');
    var scale = [];
    var mode = baseMode;
    var chromaticStep = 0;
    var baseChromatic = makeNewChromatic();
    for(var modeIndex = 0; modeIndex < modes.length; modeIndex++) {
        for(var scaleStep = 0;scaleStep <= mode.length; scaleStep++) {
            scale[scaleStep] = baseChromatic[chromaticStep];
            chromaticStep += mode[scaleStep];
        }
        scalePara[modeIndex].innerHTML = modes[modeIndex] + ": " + scale.join(" ");
        mode = changeModes(modeIndex + 1);
        chromaticStep = 0;
    }
}
changeLabel();
buildScales();
document.getElementById('notes').addEventListener('change', changeLabel);
document.getElementById('notes').addEventListener('change', buildScales);
