// scripts.js

function openTab(event, tabId) {
    var tabContents = document.getElementsByClassName("tab-content");
    for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }
    var tabButtons = document.getElementsByClassName("tab-button");
    for (var i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove("active");
    }
    document.getElementById(tabId).style.display = "block";
    event.currentTarget.classList.add("active");
}

function editArtist(artist) {

    const modal = document.getElementById("editModal");
    modal.style.display = "block";

    document.getElementById("artistId").value = artist.id;
    document.getElementById("imie_nazwisko").value = artist.imie_nazwisko;
    document.getElementById("data_urodzenia").value = artist.data_urodzenia;
    document.getElementById("data_smierci").value = artist.data_smierci || '';
}


function closeModal(id) {
    const modal = document.getElementById(id);
    modal.style.display = "none";
}


function saveChangesArtist(event) {
    event.preventDefault();

    const form = document.getElementById("editForm");
    const formData = new FormData(form);
    const updatedData = Object.fromEntries(formData.entries());

    console.log("Updated artist data:", updatedData);

    
    closeModal('editModal');
}


function saveChangesRoom(event) {
    event.preventDefault();

    const form = document.getElementById("editRoomForm");
    const formData = new FormData(form);
    const updatedData = Object.fromEntries(formData.entries());

    console.log("Updated artist data:", updatedData);

    closeModal('editRoomModal');
}


function editRoom(room) {

    const modal = document.getElementById("editRoomModal");
    modal.style.display = "block";

    document.getElementById("roomId").value = room.id;
    document.getElementById("room_name").value = room.nazwa_galerii;
}
