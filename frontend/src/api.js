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
    fetchCsv: async (fileId, page) => {
        const resp = await fetch(API_URL + "/fetch-csv/" + fileId + "?" + new URLSearchParams({
            page: page
        }))
        const json = await resp.json()
        return json
    },
    groupByCsv: async (fileId, filters) => {
        const resp = await fetch(API_URL + "/group-by-csv/" + fileId + "?" + new URLSearchParams({
            fields: filters.join(",")
        }))
        const json = await resp.json()

        return json
    }
}

export {
    apiClient
}