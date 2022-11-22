window.addEventListener("load", function ()
{
    // get button element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // Counter value.
    let counter = 0;

    // click button function.
    let clickButtonFunction = function ()
    {
        // increment counter.
        counter++;

        // update click counter value.
        clickCounterElement.innerHTML = counter;
    };

    // attach click button.
    clickButtonElement.addEventListener("click", clickButtonFunction);
});