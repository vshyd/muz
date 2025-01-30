// scripts.js


function display_message(message) {
    const successMessage = document.getElementById("success-message");
    successMessage.style.display = "block";
    successMessage.textContent = message;
    setTimeout(() => {
        successMessage.style.display = "none";
    }, 3000);

}

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

async function saveArtist(event) {
    event.preventDefault();

    const form = document.getElementById("addArtistForm");
    const formData = new FormData(form);
    dataArtist = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/admin/save_new_artist', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                artist: dataArtist
            })
        });

        const data = await response.json();
        display_message(data.message)
        closeModal('addArtistModal');
        location.reload()
    } catch (error) {
        console.error("Error Adding new Artist:", error);
    }

    
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
    
    closeModal('editModal');
}


function saveChangesRoom(event) {
    event.preventDefault();

    const form = document.getElementById("editRoomForm");
    const formData = new FormData(form);
    const updatedData = Object.fromEntries(formData.entries());

    closeModal('editRoomModal');
}


function editRoom(room) {

    const modal = document.getElementById("editRoomModal");
    modal.style.display = "block";

    document.getElementById("roomId").value = room.id;
    document.getElementById("room_name").value = room.nazwa_galerii;
}


async function openModal(galleryId, galleryName) {
    selectedGalleryId = galleryId;

    document.getElementById("modal-title").innerText = `Assign Exponat to ${galleryName}`;
    document.getElementById("assignModal").style.display = "block";

    // Fetch exponats and populate dropdown
    try {
        const response = await fetch('/admin/get_exponats');
        const exponats = await response.json();
        const select = document.getElementById("exponat-select");
        select.innerHTML = "";

        exponats.forEach(exponat => {
            const option = document.createElement("option");
            option.value = exponat.id;
            option.textContent = exponat.tytul;
            select.appendChild(option);
        });

    } catch (error) {
        console.error("Error fetching exponats:", error);
    }
}


async function assignExponat() {
    const exponatId = document.getElementById("exponat-select").value;

    try {
        const response = await fetch('/admin/assign_exponat', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                gallery_id: selectedGalleryId,
                exponat_id: parseInt(exponatId)
            })
        });

        const data = await response.json();
        display_message(data.message)
        
        closeModal('assignModal');
    } catch (error) {
        console.error("Error assigning exponat:", error);
    }
}


function displayAddModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = "block";
}


async function saveInstitution(event) {
    event.preventDefault();

    const form = document.getElementById("addInstitutionForm");
    const formData = new FormData(form);
    dataInstitution = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/admin/save_new_institution', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                institution: dataInstitution
            })
        });

        const data = await response.json();
        display_message(data.message)
        closeModal('addInstitutionModal');
        location.reload()
    } catch (error) {
        console.error("Error Adding new Institution:", error);
    }
}
