setTimeout(() => {
    const notification = document.getElementById('notification');
    notification.style.display = "none";
}, 3000);


const addcounter = (id) => {
    const counter = document.getElementById('id');
    let currentvalue = parseInt(counter.innerHTML);
    newvalue = currentvalue + 1;
    counter.innerHTML = newvalue;
}

const showbrands = () => {
    const brandlist = document.getElementById('brandlist');
    if (brandlist.style.display == ""){
        brandlist.style.display = "none";
    }
    else {
        brandlist.style.display = "";
    };
}


const showcategories = () => {
    const categories = document.getElementById('categories');
    if (categories.style.display == ""){
        categories.style.display = "none";
    }
    else {
        categories.style.display = "";
    };
}