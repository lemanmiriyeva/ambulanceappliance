const ModalLogic = {
    url: `${location.origin}/api/contact/`,

    addContact(first_name, phone, email, address, zipcode) {
        return fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                first_name,
                phone,
                email,
                address,
                zipcode,
            }),
        })
            .then((response) => {
                return response.json();
            }
            )
    },
};


const addToContact = document.getElementById('contact-form-button');
addToContact.onclick = function (e) {
    const first_name = document.getElementById('contact-form-name').value;
    const phone = document.getElementById('contact-form-phone').value;
    const email = document.getElementById('contact-form-email').value;
    const address = document.getElementById('contact-form-address').value;
    const zipcode = document.getElementById('contact-form-zipcode').value;
    ModalLogic.addContact(first_name, phone, email, address, zipcode);
    document.getElementById('modal-body').style.display = 'none';
    document.getElementById('modal-content').innerHTML = `
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-capitalize" id="exampleModalLabel">Thanks for your message!</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                ` 
    e.preventDefault();
};

const clickToCall = document.getElementById('call-local-expert')
clickToCall.addEventListener('click', function() {
    const quantity = 1
    fetch(`${location.origin}/api/statistic/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken"),
        },
        body: JSON.stringify({
            'quantity': quantity,
        })
    })
})

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
       var c = ca[i];
       while (c.charAt(0)==' ') c = c.substring(1);
       if(c.indexOf(name) == 0)
          return c.substring(name.length,c.length);
    }
    return "";
}