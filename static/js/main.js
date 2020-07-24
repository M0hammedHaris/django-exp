var firebaseConfig = {
    apiKey: "AIzaSyC56e4Okoq-J-RB7oI8nZF60cnSefvCU2I",
    authDomain: "oma-logistics.firebaseapp.com",
    databaseURL: "https://oma-logistics.firebaseio.com",
    projectId: "oma-logistics",
    storageBucket: "oma-logistics.appspot.com",
    messagingSenderId: "181250100262",
    appId: "1:181250100262:web:2fb66fdb47d1e90f9c6ae7",
    measurementId: "G-10BFJ0QQ4Z"
    };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();


var messageRef = firebase.database().ref('messages');



document.getElementById('contactForm').addEventListener('submit', submitForm);

function submitForm(e){
    alert("Form Submitted Thank You We'll call you within few hours.")

    e.preventDefault();
    var name = getInputVal('name');
    var email = getInputVal('email');
    var phone = getInputVal('phone');
    var message = getInputVal('message');
    saveMessages(name,email,phone,message);
}

function getInputVal(id){
    return document.getElementById(id).value;

}


function saveMessages(name, email, phone, message){
    var newMessageRef = messageRef.push();
    newMessageRef.set({
        name : name,
        email : email,
        phone : phone,
        message : message

    });

}