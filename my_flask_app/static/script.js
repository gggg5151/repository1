let clickCount = {{ click_count }};

document.getElementById('clickButton').addEventListener('click', function() {
    clickCount++;
    document.getElementById('countDisplay').innerText = clickCount;

    // サーバーにカウントを送信
    fetch('/increment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ count: clickCount })
    });
});
