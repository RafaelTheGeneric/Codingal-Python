var myForm = document.getElementById("myForm")
var myInput = document.getElementById("myInput")
var myItem = document.getElementById("myItem")


myForm.addEventListener("submit",function(event) {
    event.preventDefault();
    createItem(myInput.value)
})


function createItem(inputItems) {
    var itemHTML = `<li>${inputItems}
        <button onclick="deleteElement(this)">Delete</button>
    <li>`;
    myInput.insertAdjacentHTML("beforeend", itemHTML)
    myItem.value = "";
    myInput = focus();
}


function deleteElement(elementToDelete) {
    elementToDelete.parentElement.remove();
}