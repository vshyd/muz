// scripts.js


function display_message(message) {
    const successMessage = document.getElementById("success-message");
    successMessage.style.display = "block";
    successMessage.textContent = message + ". Please refresh the page";
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
            option.value = exponat.expid;
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

function editExponat(exponat){
    displayAddModal('editExponatModal')
    const fields = ["expid", "tytul", "artysta_id", "wysokosc", "szerokosc", "waga"];
    assignValuesToEditModal(exponat, fields)
}

function editRoom(room) {
    displayAddModal("editRoomModal")
    const fields = ["roomid", "nazwa_galerii"]
    assignValuesToEditModal(room, fields)
}

function editArtist(artist) {
    displayAddModal('editModal')
    const fields = ["id", "imie_nazwisko", "data_urodzenia", "data_smierci"];
    assignValuesToEditModal(artist, fields)
}

function editInstitution(institution) {
    console.log(institution)
    displayAddModal("editInstitutionModal")
    const fields = ["instid", "nazwa", "miasto"]
    assignValuesToEditModal(institution, fields)
}


function assignValuesToEditModal(obj, fields){
    fields.forEach((field) => {
        const input = document.getElementById(field);
        if (input) {
            input.value = obj[field] || "";
        }
    });
}

function displayAddModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = "block";
}


async function saveEntity(event, formId, endpoint, modalId, method) {
    event.preventDefault();

    const form = document.getElementById(formId);
    if (!form) {
        console.error(`Form with ID '${formId}' not found.`);
        return;
    }

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch(endpoint, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        display_message(result.message);
        closeModal(modalId);
    } catch (error) {
        console.error(`Error saving entity (${formId}):`, error);
        display_message("Failed to save. Please try again.");
    }
}


async function openRentModal(institutionId, institutionName) {
    selectedInstitutionId = institutionId;

    document.getElementById("rent-modal-title").innerText = `Rent Exhibit to ${institutionName}`;
    document.getElementById("rentModal").style.display = "block";

    // Fetch exponats and populate dropdown
    try {
        const response = await fetch('/admin/get_rent_exponats');
        const exponats = await response.json();
        console.log(exponats)
        const select = document.getElementById("rent-exponat-select");
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


async function rentExponat() {
    const exponatId = document.getElementById("rent-exponat-select").value;
    const dateStart = document.getElementById("date_start").value
    const dateEnd = document.getElementById("date_end").value
    
    try {
        const response = await fetch('/admin/rent_exponat', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                institution_id: selectedInstitutionId,
                exponat_id: parseInt(exponatId),
                date_start: dateStart,
                date_end: dateEnd
            })
        });

        const data = await response.json();
        display_message(data.message)
        
        closeModal('rentModal');
    } catch (error) {
        console.error("Error renting exponat:", error);
    }
}
