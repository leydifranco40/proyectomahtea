import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthorized:false,
  },
  mutations: {
    setIsAuth(state,isAuth){
      state.isAuthorized = isAuth;
    },
  },
});