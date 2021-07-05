const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn = document.querySelector('#sign-up-btn');
const container = document.querySelector('.container');
const login = document.querySelector('#login');

sign_up_btn.addEventListener('click', () => {
	container.classList.add("sign-up-mode");
});

login.addEventListener('click', () => {
    forms.submit['']
});
sign_in_btn.addEventListener('click', () => {
	container.classList.remove("sign-up-mode");
});