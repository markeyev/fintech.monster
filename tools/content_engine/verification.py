import os

class VerificationManager:
    @staticmethod
    def request_approval(stage_name, content):
        """
        In a local editor environment, we can present content and wait for a file-based approval
        or a simple console input.
        """
        print(f"\n========================================")
        print(f"VERIFICATION REQUIRED: {stage_name}")
        print(f"========================================\n")
        print(content)
        print(f"\n========================================")
        
        while True:
            choice = input(f"\nApprove this stage? (y/n/edit): ").lower().strip()
            if choice == 'y':
                return True, content
            if choice == 'n':
                return False, content
            if choice == 'edit':
                # Create a temporary file for the user to edit
                temp_file = f"review_{stage_name.lower().replace(' ', '_')}.md"
                with open(temp_file, "w") as f:
                    f.write(content)
                
                print(f"\nPlease edit {temp_file} and save it.")
                input("Press Enter once you have finished editing and saved the file...")
                
                with open(temp_file, "r") as f:
                    new_content = f.read()
                
                # Cleanup
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    
                return True, new_content
        return False, content
