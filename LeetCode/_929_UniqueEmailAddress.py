class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                pos = local.index('+')
                local = local[:pos]
            local = local.replace('.','')
            new_email = local+'@'+domain
            seen.add(new_email)
        
        return len(seen)
        