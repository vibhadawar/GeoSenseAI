import { Navigate } from "react-router-dom";
import { auth } from "../firebase";
import ProtectedRoute from "./components/protectedroute";

function ProtectedRoute({ children }) {
  if (!auth.currentUser) {
    return <Navigate to="/login" />;
  }

  return children;
}

export default ProtectedRoute;
