import AxiosInstance from "./AxiosInstance";

const AxiosApi = {
  // ====================================
  // auth controller
  // ====================================

  // 회원가입 여부 확인 (GET)
  memberExist: async (email) => {
    return await AxiosInstance.get(`/auth/exists/${email}`);
  },

  // 회원가입 (POST)
  memberSignUp: async (email, pwd, name) => {
    return await AxiosInstance.post("/auth/signup", { email, pwd, name });
  },

  // 로그인 (POST)
  memberLogIn: async (email, pwd) => {
    return await AxiosInstance.post("/auth/login", { email, pwd });
  },

  // 로그아웃 (POST)
  memberLogOut: async () => {
    return await AxiosInstance.post("/auth/logout");
  },

  // ====================================
  // board controller
  // ====================================

  // 게시글 작성 (POST)
  boardWrite: async (title, content) => {
    return await AxiosInstance.post("/board/write", {
      title,
      content,
    });
  },

  // 게시글 전체 목록 조회 (GET)
  boardList: async () => {
    return await AxiosInstance.get("/board/list");
  },

  // 게시글 상세 조회 (GET)
  boardDetail: async (id) => {
    return await AxiosInstance.get(`/board/${id}`);
  },

  // 게시글 수정 (PUT)
  boardUpdate: async (id, title, content) => {
    return await AxiosInstance.put(`/board/${id}`, { title, content });
  },

  // 게시글 좋아요 (POST)
  boardLike: async (id, email = localStorage.getItem("email")) => {
    return await AxiosInstance.post(`/board/${id}/like`, { email });
  },

  // 게시글 페이징 조회 (GET)
  boardListPage: async (page, size) => {
    return await AxiosInstance.get("/board/list/page", {
      params: { page, size },
    });
  },

  // 게시글 검색 (GET)
  boardSearch: async (page, size, keyword, type) => {
    return await AxiosInstance.get("/board/search", {
      params: { page, size, keyword, type },
    });
  },

  // 게시글 삭제 (DELETE)
  boardDelete: async (id) => {
    return await AxiosInstance.delete(`/board/${id}`);
  },

  // ====================================
  // member controller
  // ====================================

  // 회원 전체 조회 (GET)
  memberList: async () => {
    return await AxiosInstance.get("/member/list");
  },

  // 회원 상세 조회 (GET)
  memberDetail: async (email) => {
    return await AxiosInstance.get(`/member/${email}`);
  },

  // 회원 목록 페이징 조회 (GET)
  memberListPage: async (page, size) => {
    return await AxiosInstance.get("/member/list/page", {
      params: { page, size },
    });
  },

  // 내가 쓴 게시글 조회 (GET)
  myBoardList: async (email, page, size) => {
    return await AxiosInstance.get(`/member/${email}/boards`, {
      params: { page, size },
    });
  },

  // 내가 쓴 댓글 조회 (GET)
  myCommentList: async (email, page, size) => {
    return await AxiosInstance.get(`/member/${email}/comments`, {
      params: { page, size },
    });
  },

  // 회원 정보 수정 (PUT)
  memberUpdate: async (email, name, image) => {
    return await AxiosInstance.put("/member/modify", {
      email,
      name,
      image,
    });
  },

  // 회원 삭제 (DELETE)
  memberDelete: async (email) => {
    return await AxiosInstance.delete(`/member/${email}`);
  },

  // ====================================
  // comment controller
  // ====================================

  // 댓글 목록 조회 (GET)
  commentList: async (boardId) => {
    return await AxiosInstance.get(`/comment/list/${boardId}`);
  },

  // 댓글 작성 (POST)
  commentWrite: async (content, boardId) => {
    return await AxiosInstance.post("/comment/write", {
      content,
      boardId,
    });
  },

  // 댓글 수정 (PUT)
  commentUpdate: async (id, content, boardId) => {
    return await AxiosInstance.put(`/comment/${id}`, {
      content,
      boardId,
    });
  },

  // 댓글 삭제 (DELETE)
  commentDelete: async (id) => {
    return await AxiosInstance.delete(`/comment/${id}`);
  },

  // ====================================
  // chat controller
  // ====================================

  // 채팅방 생성 (POST)
  chatCreate: async (name) => {
    return await AxiosInstance.post(`/chat/new`, { name });
  },

  // 채팅방 목록 (GET)
  chatList: async () => {
    return await AxiosInstance.get(`/chat/list`);
  },

  // 채팅방 정보 (GET)
  chatRoom: async (roomId) => {
    return await AxiosInstance.get(`/chat/room/${roomId}`);
  },

  // 카카오 로그인
  kakaoLogin: async (code) => {
    return await AxiosInstance.post(`/auth/kakao`, { code });
  },
};

export default AxiosApi;
