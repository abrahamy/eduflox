export const Actions = {
  SendError: "sendError",
  HandleAsyncAError: "handleAsyncAError",
  // List
  GetAllSchools: "getAllSchools",
  GetAllServices: "getAllServices",
  // Create
  AddNewSchool: "addNewSchool",
  AddNewService: "addNewService",
  // Read
  GetSchool: "getSchool",
  GetService: "getService",
  // Update
  UpdateExistingSchool: "updateExistingSchool",
  UpdateExistingService: "updateExistingService",
  // Delete
  DeleteExistingSchool: "deleteExistingSchool",
  DeleteExistingService: "deleteExistingService",
  // Others
  ApproveOrRejectSchool: "approveOrRejectSchool"
};

export const Mutations = {
  SetIsLoading: "setIsLoading",
  SetSchools: "setSchools",
  SetServices: "setServices",
  SetErrorMessage: "setErrorMessage"
};

export const API = {
  agents: "/api/agents/",
  invitations: "/api/invitations/",
  invoices: "/api/invoices/",
  schools: "/api/schools/",
  services: "/api/services/"
};

export const Status = {
  Approved: "approved",
  Pending: "pending",
  Rejected: "rejected"
};
