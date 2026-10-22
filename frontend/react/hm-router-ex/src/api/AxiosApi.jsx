import axios from "axios"; // 비동기 통신 라이브러리

const HM_DOMAIN = "http://localhost:8111";

const AxiosApi = {
  // ====================================
  // auth controller
  // ====================================

  // 회원가입 여부 확인 (GET)
  memberExist: async (email) => {
    return await axios.get(HM_DOMAIN + `/auth/exists/${email}`);
  },

  // 회원가입 (POST)
  memberSignUp: async (email, pwd, name) => {
    return await axios.post(HM_DOMAIN + `/auth/signup`, { email, pwd, name });
  },

  // 로그인 (POST)
  memberLogIn: async (email, pwd) => {
    return await axios.post(HM_DOMAIN + `/auth/login`, { email, pwd });
  },

  // ====================================
  // board controller
  // ====================================
  // 게시글 작성 (POST)
  boardWrite: async (title, content, email) => {
    return await axios.post(HM_DOMAIN + `/board/write`, {
      title,
      content,
      email,
    });
  },

  // 게시글 전체 목록 조회 (GET)
  boardList: async () => {
    return await axios.get(HM_DOMAIN + `/board/list`);
  },

  // 게시글 상세 조회 (GET)
  boardDetail: async (id) => {
    return await axios.get(HM_DOMAIN + `/board/${id}`);
  },

  // 게시글 수정 (PUT)
  boardUpdate: async (id, title, content) => {
    return await axios.put(HM_DOMAIN + `/board/${id}`, { title, content });
  },

  // 게시글 좋아요 (POST)
  boardLike: async (id) => {
    return await axios.post(HM_DOMAIN + `/board/${id}/like`);
  },

  // 게시글 페이징 조회 (GET)
  boardListPage: async (page, size) => {
    return await axios.get(HM_DOMAIN + `/board/list/page`, {
      params: { page, size },
    });
  },

  // 게시글 검색 (GET)
  boardSearch: async (page, size, keyword, type) => {
    return await axios.get(HM_DOMAIN + `/board/search`, {
      params: { page, size, keyword, type },
    });
  },

  // 게시글 삭제 (DELETE)
  boardDelete: async (id) => {
    return await axios.delete(HM_DOMAIN + `/board/${id}`);
  },

  // ====================================
  // member controller
  // ====================================
  // 회원 전체 조회 (GET)
  memberList: async () => {
    return await axios.get(HM_DOMAIN + `/member/list`);
  },

  // 회원 상세 조회 (GET)
  memberDetail: async (email) => {
    return await axios.get(HM_DOMAIN + `/member/${email}`);
  },

  // 회원 목록 페이징 조회 (GET)
  memberListPage: async (page, size) => {
    return await axios.get(HM_DOMAIN + `/member/list/page`, {
      params: { page, size },
    });
  },

  // 내가 쓴 게시글 조회 (GET)
  myBoardList: async (email, page, size) => {
    return await axios.get(HM_DOMAIN + `/member/${email}/boards`, {
      params: { page, size },
    });
  },

  // 내가 쓴 댓글 조회 (GET)
  myCommentList: async (email, page, size) => {
    return await axios.get(HM_DOMAIN + `/member/${email}/comments`, {
      params: { page, size },
    });
  },

  // 회원 정보 수정 (PUT)
  memberUpdate: async (email, name, image) => {
    return await axios.put(HM_DOMAIN + `/member/modify`, {
      email,
      name,
      image,
    });
  },

  // 회원 삭제 (DELETE)
  memberDelete: async (email) => {
    return await axios.delete(HM_DOMAIN + `/member/${email}`);
  },

  // ====================================
  // comment board
  // ====================================
  // 댓글 목록 조회 (GET)
  commentList: async (boardId) => {
    return await axios.get(HM_DOMAIN + `/comment/${boardId}`);
  },

  // 댓글 작성 (POST)
  commentWrite: async () => {
    return await axios.get(HM_DOMAIN + `/comment/write`);
  },

  // 댓글 수정 (PUT)
  commentUpdate: async (id) => {
    return await axios.put(HM_DOMAIN + `/comment/update/${id}`);
  },

  // 댓글 삭제 (DELETE)
  commentDelete: async (id) => {
    return await axios.delete(HM_DOMAIN + `/comment/delete/${id}`);
  },
};

export default AxiosApi;
