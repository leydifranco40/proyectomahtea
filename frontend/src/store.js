import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedSer: null,
    isAuthorized:false,
  },
  mutations: {
    setSelectedSer(state, pc) {
      state.selectedPc = pc;
    },
    setIsAuth(state,isAuth){
      state.isAuthorized = isAuth;
    },
  },
});