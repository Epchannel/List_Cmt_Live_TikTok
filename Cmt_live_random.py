var baseXpath = "//*[@id='tiktok-live-main-container-id']/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div[3]";
var githubRawContentUrl = 'https://raw.githubusercontent.com/Epchannel/List_Cmt_Live_TikTok/main/cmt.txt'; // Replace with your GitHub raw content URL

// Function to fetch content from GitHub
function fetchContentFromGitHub(url) {
  return fetch(url).then(response => {
    if (response.ok) return response.text();
    throw new Error('Network response was not ok.');
  });
}

// Function to get a DOM element using XPath
function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

// Function to shuffle an array
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Fetch content from GitHub and send messages randomly
fetchContentFromGitHub(githubRawContentUrl).then(contents => {
  var contentEditableDiv = getElementByXpath(baseXpath + "/div[1]/div/div[1]/div");
  var sendButton = getElementByXpath(baseXpath + "/div[2]");

  if (contentEditableDiv && sendButton) {
    // Function to set content and send
    function setContentAndSend(content) {
      contentEditableDiv.textContent = content; // Set content to the contenteditable div
      sendButton.click(); // Click the send button
    }

    // Split the contents by new line and shuffle the array
    var contentsArray = contents.split('\n');
    shuffleArray(contentsArray);

    // Loop through the shuffled contents array and send each line
    contentsArray.forEach((content, index) => {
      setTimeout(() => {
        setContentAndSend(content);
      }, index * 60000); // Set a 1-minute delay between each send
    });
  } else {
    console.error('Cannot find contenteditable div or send button with the given XPath.');
  }
}).catch(error => {
  console.error('There was a problem fetching the GitHub content: ', error);
});
