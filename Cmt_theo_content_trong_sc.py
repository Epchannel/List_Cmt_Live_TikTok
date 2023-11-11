// Danh sách nội dung bạn muốn đặt vào div contenteditable
var contents = ["Hi", "Xin chào"];
var baseXpath = "//*[@id='tiktok-live-main-container-id']/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div[3]";

// Hàm để lấy phần tử DOM sử dụng XPath
function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

// Lấy phần tử div contenteditable và button gửi
var contentEditableDiv = getElementByXpath(baseXpath + "/div[1]/div/div[1]/div");
var sendButton = getElementByXpath(baseXpath + "/div[2]");

// Kiểm tra nếu cả div contenteditable và button gửi đều tồn tại
if (contentEditableDiv && sendButton) {
    // Hàm để đặt nội dung và gửi
    function setContentAndSend(content) {
        contentEditableDiv.textContent = content; // Điền nội dung vào div contenteditable
        sendButton.click(); // Click vào button gửi
    }

    // Lặp qua danh sách nội dung và áp dụng hàm
    contents.forEach(function(content, index) {
        setTimeout(function() {
            setContentAndSend(content);
        }, index * 60000); // Đặt một độ trễ 1 phút giữa mỗi gửi
    });
} else {
    console.error('Không thể tìm thấy div contenteditable hoặc button gửi với XPath đã cho.');
}
