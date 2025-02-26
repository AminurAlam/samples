const passwords = {
  aa: "aa",
  ss: "ss",
  dd: "dd",
  ff: "ff",
};

function signup() {
  var un = username.value;
  var pass = password.value;
  var dob = dob.value;
  var email = email.value;
}

function login() {
  var un = username.value;
  var pass = password.value;

  if (un in passwords) {
    if (passwords[un] == pass) {
      window.location = `/user/${un}`;
    } else {
      window.alert("wrong password!!");
    }
  } else {
    window.alert(`username ${un} not found!!`);
  }
}
