// // When the timer last ran.
// let lastRan = new Date();

// Keeping track of which line is highlighted.
let highlighted = null;
// Making this a function so that this crude styling can be changed later. :-)
function highlight(text) {
    if (highlighted) highlighted.classList.remove('line-being-read');
    text.classList.add('line-being-read');
    text.scrollIntoView({ behavior: "smooth", block: "center" });
    highlighted = text;
}

// The "main" of this script.
{
    // Set up handlers for click on text
    for (const line of document.getElementsByClassName('line-rame')) {
        const begin = line.getAttribute('begin');
        line.addEventListener('click', (e) => {
            document.getElementById("rame-audio").currentTime = parseFloat(begin);
        });
    }
    // Set up handlers for time change in audio.
    // Note: This event can fire several times a second, so keep this handler light.
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event
    document.getElementById('rame-audio').ontimeupdate = (event) => {
        // // Don't run this more than every 100 ms.
        // if (new Date() - lastRan < 100) return;
        // lastRan = new Date();
        const whatTime = document.getElementById("rame-audio").currentTime;
        // Find the right text. For now, O(n) loop is fine; we have at most a few hundred verses in a sarga.
        let seenLine = null;
        for (const text of document.getElementsByClassName('line-rame')) {
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
