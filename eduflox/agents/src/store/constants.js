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
  UpdateExistingService: "updateExistingService"
};

export const Mutations = {
  SetIsLoading: "setIsLoading",
  SetSchools: "setSchools",
  SetErrorMessage: "setErrorMessage"
};

export const API = {
  agents: "/api/agents/",
  invitations: "/api/invitations/",
  invoices: "/api/invoices/",
  schools: "/api/schools/",
  services: "/api/services/"
};

export const TableColumns = {
  SchoolTableColumns: [
    {
      field: "name",
      label: "Name",
      sortable: true
    },
    {
      field: "code",
      label: "Code",
      sortable: true
    },
    {
      field: "location",
      label: "Location",
      sortable: true
    },
    {
      field: "district",
      label: "District",
      sortable: true
    },
    {
      field: "status",
      label: "Status",
      sortable: true
    },
    {
      field: "created_at",
      label: "Date Created",
      sortable: true,
      centered: true
    }
  ],
  ServiceTableColumns: []
};
