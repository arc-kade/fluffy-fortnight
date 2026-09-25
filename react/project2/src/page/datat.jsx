import { useEffect, useState } from "react";

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts/")
      .then((response) => response.json())
      .then((result) => setData(result));
  }, []);

  return (
    <div>
      {data ? (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(4, 1fr)",
            gap: "16px",
            padding: "16px"
          }}
        >
          {data.slice(0, 100).map((datas) => (
            <div
              key={datas.id}
              style={{
                border: "1px solid #ccc",
                padding: "12px",
                borderRadius: "8px"
              }}
            >
              <h4 style={{ margin: "0 0 8px 0" }}>{datas.title}</h4>
              <p style={{ margin: 0, fontSize: "14px" }}>{datas.body}</p>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default DataFetcher;