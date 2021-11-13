const API_URL = "http://127.0.0.1:8000/api"

const apiClient = {
    fetchFiles: async () => {
        const resp = await fetch(API_URL + "/files/")
        const json = await resp.json()
        return json.items
    },
    fetch: () => {
        return fetch(API_URL + "/fetch/")
    },
    fetchCsv: (fileId) => {
        return fetch(API_URL + "/fetch-csv/" + fileId + "/")
    },
    groupByCsv: (fileId) => {
        return fetch(API_URL + "/group-by-csv/" + fileId + "/")
    }
}

export {
    apiClient
}