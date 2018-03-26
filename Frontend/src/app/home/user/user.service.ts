import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

const routes = {
  user: () => `/user/`
};


@Injectable()
export class UserService {

  constructor(private httpClient: HttpClient) {
  }

  user(userName: string): Observable<any> {
    return this.httpClient
      .post(routes.user(), {'user_name': userName});
  }

}
