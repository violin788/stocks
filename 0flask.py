# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Copy Text to Clipboard</title>
    <script>
        function open_login_portals() {
            const websites = [
            "https://chat.openai.com",
            "https://open.spotify.com/show/030JakQMatQTMOIkwVx2cQ",
            "https://account.proton.me/mail",
            "https://www.facebook.com",
            "https://www.reddit.com/login/",
            "https://x.com/i/flow/login",
            "https://drive.google.com/drive/home",
            "https://reimagined-space-happiness-wrxv7r67wgx939wpp.github.dev/"
            ];
            // Open each website in a new tab
            websites.forEach(url => {
                window.open(url, "_blank");
            });
        }
        function open_already_in() {
            const websites = [
            "https://chat.openai.com",
            "https://open.spotify.com/show/030JakQMatQTMOIkwVx2cQ",
            "https://account.proton.me/mail",
            "https://www.facebook.com",
            "https://www.reddit.com",
            "https://x.com",
            "https://www.drive.google.com",
            "https://ideal-xylophone-jjrp7qqqx994374j.github.dev/"
            ];
            // Open each website in a new tab
            websites.forEach(url => {
                window.open(url, "_blank");
            });
        }
        // Array of text items
        const texts = [
            "media788788@gmail.com",
            "Medmed2@",
            "ballotamend",
            "votevote",
            "know357",
            "know3333",
            "violin78@protonmail.com",
            "Viovio2@",
        ];
        function copyTextToClipboard(text) {
            // Create a temporary input element
            var tempInput = document.createElement("input");
            tempInput.value = text; // Set the text to the input
            // Append the input to the body
            document.body.appendChild(tempInput);
            // Select the text
            tempInput.select();
            tempInput.setSelectionRange(0, 99999); // For mobile devices
            // Copy the text to the clipboard
            document.execCommand("copy");
            // Remove the temporary input element
            document.body.removeChild(tempInput);
        }
        function generateList() {
            const listContainer = document.getElementById("listContainer");
            texts.forEach((text, index) => {
                const div = document.createElement("div");
                div.innerHTML = `<span>${text}</span> <button onclick="copyTextToClipboard('${text}')">Copy</button>`;
                listContainer.appendChild(div);
            });
        }
        function openURL(url) {
            window.open(url, '_blank');
        }

        function get_marketplace_url() {
        // Get the values from the form fields
        var search_for = document.getElementById("marketplace_search").value;
        var baseUrl = "https://www.facebook.com/marketplace/103795126325698/search?deliveryMethod=local_pick_up&sortBy=price_ascend&query=";
        var url = baseUrl + search_for + "&exact=false";
        window.open(url, '_blank');
      }

        function get_ebay_url() {
        // Get the values from the form fields
        var search_for = document.getElementById("ebay_search").value;
        var url = "https://www.ebay.com/sch/i.html?_nkw="+search_for+"&_sacat=0&_from=R40&_sadis=25&_stpos=22401&_fspt=1&_sop=15&_blrs=recall_filtering";
        window.open(url, '_blank');
      }

        function updateURL() {
            let searchTerm = document.getElementById("searchInput").value.trim();
            if (searchTerm) {
                let baseUrl = "https://www.facebook.com/marketplace/103795126325698/search?deliveryMethod=local_pick_up&sortBy=price_ascend&query=";
                let newUrl = baseUrl + encodeURIComponent(searchTerm) + "&exact=false";
                window.location.href = newUrl; // Redirect to new URL
            }
        }
        window.onload = generateList; // Call the function to generate the list when the page loads
        document.addEventListener("DOMContentLoaded", function () {
            const buttons = [
                { text: "bannon war room", url: "https://rumble.com/BannonsWarRoom" },
                { text: "newsmax2", url: "https://rumble.com/c/NewsmaxTV" },
                { text: "vidwud", url: "https://www.vidwud.com/free-face-swap.html" },
                { text: "aiswap.io", url: "https://aifaceswapper.io/video-face-swap" },
                { text: "twitter media downloader", url: "https://ssstwitter.com/" },
                { text: "youtube media downloader", url: "https://ezmp3.cc/71m8" },
                { text: "python anywhere login", url: "https://www.pythonanywhere.com/login/?next=/" },
                { text: "send anywhere", url: "https://send-anywhere.com/" },
                { text: "weather radar", url: "https://weather.com/weather/radar/interactive/l/Fredericksburg+VA?canonicalCityId=08a051206dd97b486cb0128338def846c6fcec0d29766b8f97755b41321b1215" },
                { text: "weather", url: "https://www.google.com/search?q=weather&rlz=1CANCLQ_enUS1152&oq=weather&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAtIBCDEwMjlqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8" },
                { text: "cnbc", url: "https://www.cnbc.com/" },
                { text: "thestreet.com", url: "https://www.thestreet.com/" },

            ];
            const container = document.getElementById("buttonContainer");
            buttons.forEach(button => {
                const btn = document.createElement("button");
                btn.textContent = button.text;
                btn.onclick = () => window.open(button.url, "_blank");
                container.appendChild(btn);
                container.appendChild(document.createElement("br")); // Add first line break
            });
        });
function get_option() {
    // Get the values from the form fields
    var symbol = document.getElementById("symbol").value;
    var price = document.getElementById("price").value;
    var type = document.getElementById("type").value;
    // Determine the option type (P for Put, C for Call)
    var optionType = (type === "call") ? "C" : "P";
    // Get today's date
    var today = new Date();
    var dayOfWeek = today.getDay(); // 0 (Sunday) to 6 (Saturday)
    // Calculate next Friday's date
    var daysUntilFriday = (dayOfWeek === 5) ? 0 : (5 - dayOfWeek + (dayOfWeek > 5 ? 7 : 0));
    var nextFriday = new Date();
    nextFriday.setDate(today.getDate() + daysUntilFriday);
    // Format next Friday as YYMMDD
    var yy = nextFriday.getFullYear().toString().slice(-2);
    var mm = String(nextFriday.getMonth() + 1).padStart(2, '0');
    var dd = String(nextFriday.getDate()).padStart(2, '0');
    var formattedDate = yy + mm + dd;
    // Build the URL
    var url = "https://www.tradingview.com/chart/?symbol=OPRA%3A" + symbol + formattedDate + optionType + price + ".0";
    window.open(url, '_blank');
}
    function get_stock() {
    // Get the values from the form fields
    var symbol = document.getElementById("symbol_stock_lookup").value;
    var url = "https://www.tradingview.com/chart/?symbol=NYSE%3A"+symbol;
    window.open(url, '_blank');
  }
    </script>
</head>
<body>
    <div id="listContainer"></div><br>
    <button onclick="open_login_portals()">login pages</button><br>
    <button onclick="open_already_in()">already loaded</button><br>
    <div id="buttonContainer"></div>
      <div class="container">
        <div class="form-container">
          <form id="optionForm">
            <input type="text" id="symbol" placeholder="Stock Symbol" required>
            <select id="type" required>
              <option value="call">Call</option>
              <option value="put">Put</option>
            </select>
            <input type="number" id="price" placeholder="Options Price" required>
            <button type="button" onclick="get_option()">get options diagram</button><br>
            <input type="text" id="symbol_stock_lookup" placeholder="tradingview stock symbol lookup" required>
            <button type="button" onclick="get_stock()">get stock history</button><br>

          </form>
        </div>
        <div class="result-container" id="result"></div>
      </div>
      <div class="result-container" id="result"></div>
    <input type="text" id="marketplace_search" placeholder="fb marketplace search">
    <button onclick="get_marketplace_url()">look for item!</button>
    <br>
    <input type="text" id="ebay_search" placeholder="ebay search">
    <button onclick="get_ebay_url()">look for item!</button>
    <a id="searchLink" href="" target="_blank"></a>
</body>
</html>
    """




