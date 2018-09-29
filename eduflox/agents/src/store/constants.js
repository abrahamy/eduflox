export const Actions = {
  CallBackend: "apiCall",
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
  DeleteExistingService: "deleteExistingService"
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
