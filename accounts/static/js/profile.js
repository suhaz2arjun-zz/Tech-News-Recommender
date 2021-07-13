const update = document.querySelector('.update');
const userDetails = document.querySelector('.media-body');
const updateSection = document.querySelector('.update-section');
const saveBtn = document.querySelector('.save-btn');
const alertMsg = document.querySelector(".alert");
const interests = document.querySelector("#div_id_interest");

const label = document.createElement('h3');
label.innerHTML = "Choose your topics"
interests.insertBefore(label,interests.firstChild)
update.addEventListener('click',(e)=>{
    e.preventDefault();
    updateSection.style.display = "block";
    userDetails.style.display = "none";
    update.style.display = "none";
})

saveBtn.addEventListener('click',()=>{
    alertMsg.style.display = "block";
})
 

