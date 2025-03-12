var accounts = {
  aa: "aa",
  ss: "ss",
  dd: "dd",
  ff: "ff",
};

function signup() {
  if (!username.value.match(/^\w+$/)) {
    window.alert("username can only contain alphanumeric charecters");
    return;
  }
  if ((!username.value) in accounts) {
    window.alert("username is already taken");
    return;
  }
  if (password.value.length < 4) {
    window.alert("password is too short");
    return;
  }
  accounts[username.values] = password.value;

  let url = new URL("/fb/", window.location.origin);
  url.pathname = `/fb/user.html`;
  url.searchParams.set("user", username.value);
  window.location.href = url.href;
  // window.location = `user.html?user=${username.value}`;
}

function login() {
  if (username.value in accounts) {
    if (accounts[username.value] == password.value) {
      window.location = `user.html?user=${username.value}`;
    } else {
      window.alert("wrong password");
    }
  } else {
    window.alert(`username ${username.value} does not exist`);
  }
}
