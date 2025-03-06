const passwords = {
  aa: "aa",
  ss: "ss",
  dd: "dd",
  ff: "ff",
};

function signup() {
  // var un = username.value;
  // var pass = password.value;
  // var dob = dob.value;
  // var email = email.value;
  if (!username.value.match(/^\w+$/)) {
    window.alert("username can only contain alphanumeric charecters");
    return;
  }
  if (password.value.length < 4) {
    window.alert("pass is too short");
    return;
  }
  window.location = `user?user=${username.value}.html`;
}

function login() {
  var un = username.value;
  var pass = password.value;

  if (un in passwords) {
    if (passwords[un] == pass) {
      window.location = `user0?user={un}.html`;
    } else {
      window.alert("wrong password!!");
    }
  } else {
    window.alert(`username ${un} not found!!`);
  }
}
