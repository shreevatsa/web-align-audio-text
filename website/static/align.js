// Keeping track of which line is highlighted.
let highlighted = null;
// Making this a function so that this crude styling can be changed later. :-)
function highlight(text) {
    if (highlighted) highlighted.style.fontWeight = '';
    text.style.fontWeight = 'bold';
    text.scrollIntoView({ block: "center"});
    highlighted = text;
}

// The "main" of this script.
{
    // Set up handlers for click on text
    for (const line of document.getElementsByClassName('line-ramayana')) {
        const begin = line.getAttribute('begin');
        line.addEventListener('click', (e) => {
            document.getElementById("audio-ramayana").currentTime = parseFloat(begin);
        });
    }
    // Set up handlers for time change in audio.
    // Note: This event can fire several times a second, so keep this handler light.
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event
    document.getElementById('audio-ramayana').ontimeupdate = (event) => {
        const whatTime = document.getElementById("audio-ramayana").currentTime;
        // Find the right text. For now, O(n) loop is fine; we have at most a few hundred verses in a sarga.
        let seenLine = null;
        for (const text of document.getElementsByClassName('line-ramayana')) {
            const thisTextStart = parseFloat(text.getAttribute('begin'));
            if (seenLine == null || thisTextStart <= whatTime) {
                seenLine = text;
            } else {
                break;
            }
        }
        if (seenLine) highlight(seenLine);
    }
}
