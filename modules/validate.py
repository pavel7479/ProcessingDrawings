class Validator:
    def validate(self, context_before, context_after):
        return len(context_before.get("numbers", [])) == len(
            context_after.get("numbers", [])
        )
