class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        for email in emails:
            local, domain = email.split('@')
            name = local.split('+')[0].replace('.','')
            st.add(name + '@' + domain)
        return len(st)
        
        # for email in emails:
        #     local, domain = email.split('@')
        #     if '+' in local:
        #         local = local[:local.index('+')]
        #     if '.' in local:
        #         local = local.replace('.','')
        #     clean = local+ '@' + domain
        #     st.add(clean)
        # return len(st)
